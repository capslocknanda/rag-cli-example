import asyncio
import os
from urllib.parse import urlparse
from crawl4ai import *

async def main():
    # Define paths
    list_path = "./list.txt"
    output_dir = "./pages-raw"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read URLs from the list file
    with open(list_path, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]


    async with AsyncWebCrawler() as crawler:
        for url in urls:
            print(f"Deep Crawling starting from: {url}")

             # 1. Configure the deep crawl strategy
            # max_depth=2 follows links from the homepage to child pages.
            # max_pages=30 stops the crawl once 30 pages are reached.
            deep_crawl_strategy = BFSDeepCrawlStrategy(
                max_depth=5, 
                max_pages=30,
                include_external=False  # Stay within the diomain
            )

            # 2. Configure what to extract/exclude
            # We exclude images, videos, and audio to get "perfect text"
            run_config = CrawlerRunConfig(
                deep_crawl_strategy=deep_crawl_strategy,
                exclude_external_links=True,
                exclude_social_media_links=True,
                exclude_external_images=True,  # No external images
                excluded_tags=['img', 'video', 'audio', 'noscript'], # Strip media tags
                word_count_threshold=10  # Skip tiny text blocks (nav/footers)
            )

            # NOTE: results is a LIST of CrawlResult objects when using deep crawl
            results = await crawler.arun(url=url, config=run_config)
            
            for i, result in enumerate(results):
                if not result.success:
                    continue
                
                # Use result.url (the specific subpage) for the filename
                parsed_path = urlparse(result.url).path
                # Clean up filename: remove slashes and ensure it's not empty
                safe_name = parsed_path.strip("/").replace("/", "_") or f"index_{i}"
                filename = f"{safe_name}.md"
                
                output_path = os.path.join(output_dir, filename)
                
                with open(output_path, "w", encoding="utf-8") as f_out:
                    f_out.write(f"Source: {result.url}\n\n")
                    # result.markdown is a MarkdownGenerationResult object
                    # use .raw_markdown or .fit_markdown for the actual text
                    f_out.write(result.markdown.raw_markdown)
                
                print(f"  [+] Saved ({i+1}/{len(results)}): {output_path}")

if __name__ == "__main__":
    asyncio.run(main())