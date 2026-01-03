import asyncio
import uuid
import json
import os
import typer
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.markdown import Markdown
from httpx import AsyncClient, Timeout
from httpx_sse import aconnect_sse

# Setup Rich console
console = Console()

app = typer.Typer()

API_URL = os.environ.get("API_URL", "http://localhost:8000/stream")

class ChatSession:
    def __init__(self):
        self.is_continue = False
        self.thread_id = str(uuid.uuid4())

    async def stream_chat(self, query: str):
        payload = {
            "query": query,
            "is_continue": self.is_continue,
            "thread_id": self.thread_id
        }

        full_response = ""
        
        with Live(Panel("...", title="Assistant", border_style="blue"), console=console, refresh_per_second=10) as live:
            try:
                timeout = Timeout(60.0, read=None)
                async with AsyncClient(timeout=timeout) as client:
                    async with aconnect_sse(client, "POST", API_URL, json=payload) as sse:
                        async for event in sse.aiter_sse():
                            try:
                                data = json.loads(event.data)
                                chunk = data.get("text", "")
                                full_response += chunk
                                
                                live.update(Panel(Markdown(full_response), title="Assistant", border_style="blue"))
                            except json.JSONDecodeError:
                                full_response += event.data
                                live.update(Panel(Markdown(full_response), title="Assistant", border_style="blue"))
                                
            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] {e}")

        self.is_continue = True

@app.command()
def start():
    """Start the Interactive RAG Session."""
    session = ChatSession()
    
    console.print(Panel("[bold green]ViewSonic Software RAG CLI[/bold green]\nType 'exit' to quit.", expand=False))

    while True:
        query = typer.prompt("\n[User]")
        
        if query.lower() in ["exit", "quit", "q"]:
            break

        # Async streaming logic
        asyncio.run(session.stream_chat(query))

        choice = typer.confirm("Would you like to continue this conversation?", default=True)
        
        if not choice:
            session.is_continue = False
            session.thread_id = str(uuid.uuid4())
            console.print("[dim]Session reset. Next query will be a fresh start.[/dim]")
        else:
            console.print("[dim]Continuing conversation...[/dim]")

if __name__ == "__main__":
    app()