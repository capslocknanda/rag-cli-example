Source: https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements

[](https://www.viewsonic.com/)
Menu
[English](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements) [Français](https://www.viewsonic.com/solution/kb/fr_FR/entity-setup/networking-requirements) [Español](https://www.viewsonic.com/solution/kb/es_ES/entity-setup/networking-requirements) [Thai](https://www.viewsonic.com/solution/kb/th_TH/entity-setup/networking-requirements)
  * [Products](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
  * [Resources](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
[What's New](https://www.viewsonic.com/solution/kb/en_US/whats-new) [Knowledge Base](https://www.viewsonic.com/solution/kb/en_US/) [Training & Development](https://www.viewsonic.com/us/resources/myviewboard) [Recommended Hardware](https://www.viewsonic.com/us/products/shop/viewboard.html)


  * [GET IN TOUCH](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
### How Can We Help?
    * #### Technical Support
Having issues using myViewBoard? Head over to our Support page and we'll help you solve it.
#### Sales Inquiry
Want to sign up your organization, request a demo, or get training? Click the button below.


#### ViewSonic Knowledge Base
  

##  ViewSonic Account
  

## [ ViewSonic Account ](https://www.viewsonic.com/solution/kb/)


### Contact us
**No results found.** If you still have questions or prefer to get help directly from a representative, please submit a request. 
Fill out the contact form below and we'll reply as soon as possible.
  

####  [
* * * ](https://www.viewsonic.com/solution/kb/)
  * ViewSonic user account 
    * [Account overview](https://www.viewsonic.com/solution/kb/en_US/viewsonic-user-account/vs-account-overview)
    * [Account](https://www.viewsonic.com/solution/kb/en_US/viewsonic-user-account/vs-account)
    * [Notifications](https://www.viewsonic.com/solution/kb/en_US/viewsonic-user-account/vs-notifications)
    * [Security](https://www.viewsonic.com/solution/kb/en_US/viewsonic-user-account/vs-security)
    * [Subscriptions](https://www.viewsonic.com/solution/kb/en_US/viewsonic-user-account/vs-subscription)
ViewSonic entity account 
    * [About Entity Management](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-about-entity-management)
    * [Account migration FAQs](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-account-migration-faqs)
    * [Overview](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-overview)
    * [Domains](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-domains)
    * [Users](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-users)
    * [Subscriptions](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-subscriptions)
    * [Admin Roles](https://www.viewsonic.com/solution/kb/en_US/viewsonic-entity-account/vse-admin-roles)
Entity setup 
    * [Request an entity account](https://www.viewsonic.com/solution/kb/en_US/entity-setup/request-entity-account)
    * [Entity types](https://www.viewsonic.com/solution/kb/en_US/entity-setup/entity-type-breakdown)
    * [Roles after entity creation](https://www.viewsonic.com/solution/kb/en_US/entity-setup/user-roles)
    * [Networking setup](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)


#### Was this article helpful?
[](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements) [](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
Print 
# Networking setup
When setting up your ViewSonic entity, confirm that your network meets the requirements listed in this document. Each ViewSonic service has its own set of requirements designed to ensure stable performance. Use this guide to prepare and validate your network environment.
  

  

## Entity Management
Entity owners and admins should whitelist the following domains to ensure all users in the entity can run ViewSonic software without issue.
  

### Ports
Configure your firewall to allow access to ports used by various ViewSonic services.
  

**Mandatory:**
  * TCP port 443 (HTTPS): Outbound is required for general operation and activation.


  

**Wireless screen sharing requirement (optional):**
  * UDP and TCP port 3478: Bidirectional to the WebRTC servers.
  * UDP ports 50,000 – 65,535 (RTP / sRTP / RTCP): Bidirectional to the WebRTC servers.


  

  

These ports are optional. If blocked, media will be proxied using TURN on port 3478. The WebRTC protocol is only used for screen sharing. Verify that these ports are open on your network firewall if you wish to use screen sharing.
  

### **Email addresses**
Whitelist the following email addresses:
  

service@myviewboard.com | Notifications, security, and user account information.  
---|---  
letstalk@service.myviewboard.com | myViewBoard Support Team help desk email.  
myviewboard@news.myviewboard.com | myViewBoard news and promotions.  
no-reply@service.viewsonic.cloud  
no-reply@billing.viewsonic.cloud  
service@billing.viewsonic.cloud | For ViewSonic services.  
  

Whitelist the following domain names. Make sure to include the asterisks (*) as listed.
  

*myviewboard.com | Used by the web application's ecosystem  
---|---  
*myviewboard.cloud   
*.viewsonic.cloud  
cloud.viewsonic.com | Used by the web service.  
*firebaseio.com | Used by video and audio streaming features.  
*amazonaws.com | Used by AWS services.  
  

  

### IP Addresses
For North American entities only: In case connectivity issues persist, please whitelist the IPs shown below.
  * 15.197.73.244
  * 166.117.187.110
  * 166.117.110.220
  * 166.117.161.118
  * 166.117.87.214
  * 3.33.176.118


* * *
  

## Manager
Apply the following whitelist configuration to use key features of the Manager web console.
  

### Ports
Required for [Remote Control](https://www.viewsonic.com/solution/kb/managing-devices/remote-control)
  * TCP Port 443 (HTTPS)


  

Required for [Remote Desktop](https://www.viewsonic.com/solution/kb/manager-advanced-features/remote-desktop)
  * TCP 443 for mrtc.myviewboard.cloud
  * TCP 443 for getice.myviewboard.cloud


  

Allow access to the following from the internet (WAN):
  * TCP 443 for ice.myviewboard.cloud
  * TCP 3478 for ice.myviewboard.cloud
  * UDP 3478 for ice.myviewboard.cloud


  

Peer-to-peer connection should be allowed. Optional, but enables better performance:
  * 1024-65535 UDP


  

  

### Domain names
Whitelist the following domain names. Make sure to include the asterisks (*) as listed.
  

*myviewboard.com | Used by the web application's ecosystem  
---|---  
*myviewboard.cloud  
*.viewsonic.cloud  
cloud.viewsonic.com | Used by the web service.  
*firebaseio.com | Used by video and audio streaming features.  
*amazonaws.com | Used by AWS services.  
  

  

* * *
  

## myViewBoard 
Review the following whitelisting requirements for myViewBoard below. Incorrect configuration may result in screen sharing or any other feature within myViewBoard to become blocked or non-functional. 
  

**Mandatory:**
  * TCP port 443 (HTTPS): Outbound is required for general operation and activation.


  

**Wireless screen sharing requirement (optional):**
  * UDP and TCP port 3478: Bidirectional to the WebRTC servers.
  * UDP ports 50,000 – 65,535 (RTP / sRTP / RTCP): Bidirectional to the WebRTC servers.


  

* * *
  

## Display
To ensure that casting or receiving screens through myViewBoard Display runs smoothly, whitelist the following ports:
  

  

**Mandatory:**
  * TCP port 443 (HTTPS): Outbound is required for general operation and activation.


  

**Wireless screen sharing requirement (optional):**
  * UDP and TCP port 3478: Bidirectional to the WebRTC servers.
  * UDP ports 50,000 – 65,535 (RTP / sRTP / RTCP): Bidirectional to the WebRTC servers.


  

These ports are optional. If blocked, media will be proxied using TURN on port 3478. 
  

* * *
  

## Other casting solutions
ViewBoards are preloaded with multiple solutions to cast from a personal device to a ViewBoard. To ensure successful casting or receiving screens on a ViewBoard, whitelist the following ports:
  

[Delete](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
**5GHz NETWORK CONNECTION RECOMMENDED**
For optimal performance of all casting solutions that will be mentioned below, setup a network environment that supports Wi-Fi 802.11n on the 5 GHz band. Refer to a 5 GHz channel guide for non-DFS channels available in your region. In the United States, these are channels 36–48 and 149–165.
  

  

## AirSync
For optimal performance, verify that the network where AirSync and the AirSync client operates has the firewall configured to allow the following connections:
  

### Relay connection
Relay connections are used in scenarios where direct connections between devices are not possible due to network configurations.
  

**With wildcards**
  * TCP 443 for _*.myviewboard.cloud_
  * TCP 443 for _*.myviewboard.com_
  * TCP 443 for _*.viewsonic.com_
  * TCP 443 for _*.airsync.net_


  

**Without wildcards**
For firewalls that don't allow wildcards.
  

  * TCP 443 for _airsync.net_ , _www.airsync.net_ , _airsync.viewsonic.com_
  * TCP 443 for:
    * _api.gateway.airsync.net_
    * _us-east-1.gateway.airsync.net_
    * _ap-northeast-1.gateway.airsync.net_
  * TCP 443 for _appconfig.airsync.net_
  * TCP 443 for _getice.myviewboard.cloud_
  * TCP 443 for _store2.myviewboard.com_ (OTA)
  * TCP 443 for _store2.airsync.net_ (OTA)


  

**Video/Audio (WebRTC)**
  * TCP 443 for _turn.myviewboard.cloud_
  * TCP 3478 for _turn.myviewboard.cloud_
  * UDP 3478 for _turn.myviewboard.cloud_ (Optional)
  * Local UDP ports _32768~61000_


  

  

### Local Connection (Direct connection)
Establish a network connection directly between devices within the LAN without relying on external servers or services.
  * TCP 5001


  

**Remote Screen**
  * TCP 7000


  

**Video/Audio (WebRTC)**
  * Random UDP ports in the range of _32768~61000_


  

**Mirror**
AirPlay, Googlecast, and Miracast do not require access to the Internet.
  

  * _AirPlay, Google Cast_
    * Does not work in different subnet/VLAN
    * Random UDP ports in the range of  _32768~61000_  
  

  * _Miracast_
    * Use Wi-Fi Direct (WiFi P2P). Does not require wireless AP.


  

### Notes
Ephemeral port range on Android or Linux:
  

```
adb shell cat /proc/sys/net/ipv4/ip_local_port_range
```

  

  

  

**Limit WebRTC port range in Chrome**
Chrome policies (WebRtcUdpPortRange) can limit the range of local UDP ports used by WebRTC. Refer to setting UDP port ranges in the following page:
  

  

* * *
  

## vCast 
Whitelist the following ports:
  

**Ports**
  * TCP 56789, 25123, 8121 & 8000 (for controlling message port & client device audio transfer)
  * TCP 8600 (BYOM)
  * TCP53000 (Request share screen)
  * TCP52020 (Reverse control)
  * TCP52030 (Status sync)
  * UDP 48689, 25123 (Device searching and broadcast & client device audio transfer)
  * UDP 5353 (Multicast search device protocol)


  

**Ports and DNS for activation**
  * Port: 443
  * DNS: https://vcastactivate.viewsonic.com


  

**OTA service**
  * Server Port: TCP443
  * Server FQDN Name: https://vcastupdate.viewsonic.com


  

[Delete](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
**NOTE ON SUBNET CONNECTION**
Devices with the vCast software can connect to both the same subnet and across the subnet network in order to begin sending or receiving a screen.
  

## AirPlay
Whitelist the following ports:
  

  * TCP 51040, 51030, 51020 & 51010
  * UDP 5353 (mDNS to broadcast AirPlay)


  

  

## Chromecast
Whitelist the following ports:
  

  * TCP 8008 & 8009
  * UDP 5353 (mDNS to broadcast CCast)


  

  

  

  

  

[ « Previous ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/user-roles)
Next »
Contents
[Entity Management ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#entity-management-0) [Ports ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#ports-1) [Email addresses ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#email-addresses-2) [IP Addresses ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#ip-addresses-3) [Manager ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#manager-4) [Ports ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#ports-5) [Domain names ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#domain-names-6) [myViewBoard ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#myviewboard-7) [Display ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#display-8) [Other casting solutions ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#other-casting-solutions-9) [AirSync ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#airsync-10) [Relay connection ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#relay-connection-11) [Local Connection (Direct connection) ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#local-connection-direct-connection-12) [Notes ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#notes-13) [vCast ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#vcast-14) [AirPlay ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#airplay-15) [Chromecast ](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements#chromecast-16)
* * *
### Need additional help?
Check our other resources — we'll be happy to assist you.
* * *
[ ](https://www.viewsonic.com/)
  

* * *
###### myViewBoard
###### Tools
###### Solutions
###### Resources
  * [What's New](https://www.viewsonic.com/solution/kb/en_US/whats-new/)
  * [Knowledge Base](https://www.viewsonic.com/solution/kb/en_US/)


###### Socials
ViewSonic 2017-2026. © All Rights Reserved.
Sat Jan 03 2026 21:41:35 GMT+0800 (Taiwan Standard Time)
Do you have questions?   
We are here to answer. 😊
