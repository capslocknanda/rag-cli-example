Source: https://www.viewsonic.com/solution/kb/entity-management-1/software-instances

[](https://www.viewsonic.com/)
Menu
[English](https://www.viewsonic.com/solution/kb/en_US/entity-management-1/software-instances) [Français](https://www.viewsonic.com/solution/kb/fr_FR/entity-management-1/software-instances) [Español](https://www.viewsonic.com/solution/kb/es_ES/entity-management-1/software-instances) [Thai](https://www.viewsonic.com/solution/kb/th_TH/entity-management-1/software-instances)
  * [Products](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
  * [Resources](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
[What's New](https://www.viewsonic.com/solution/kb/en_US/whats-new) [Knowledge Base](https://www.viewsonic.com/solution/kb/en_US/) [Training & Development](https://www.viewsonic.com/us/resources/myviewboard) [Recommended Hardware](https://www.viewsonic.com/us/products/shop/viewboard.html)


  * [GET IN TOUCH](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
### How Can We Help?
    * #### Technical Support
Having issues using myViewBoard? Head over to our Support page and we'll help you solve it.
#### Sales Inquiry
Want to sign up your organization, request a demo, or get training? Click the button below.


####  Entity Management
  

  

All the setup tools and info to run your entity
## [ Entity Management ](https://www.viewsonic.com/solution/kb/entity-management)
All the setup tools and info to run your entity


### Contact us
**No results found.** If you still have questions or prefer to get help directly from a representative, please submit a request. 
Fill out the contact form below and we'll reply as soon as possible.
  

####  [
* * * ](https://www.viewsonic.com/solution/kb/)
  * Before creating an entity 
    * [Request an entity account](https://www.viewsonic.com/solution/kb/en_US/entity-setup/request-entity-account)
    * [Entity types](https://www.viewsonic.com/solution/kb/en_US/entity-setup/entity-type-breakdown)
    * [Roles after entity creation](https://www.viewsonic.com/solution/kb/en_US/entity-setup/user-roles)
    * [Networking setup](https://www.viewsonic.com/solution/kb/en_US/entity-setup/networking-requirements)
    * [ViewBoard Deployment Approach](https://www.viewsonic.com/solution/kb/en_US/before-creating-entity/viewboard-deployment-approach)
Other resources 
    * [Requesting Live Captions](https://www.viewsonic.com/solution/kb/en_US/other-resources-1/requesting-live-captions)
    * [Casting solutions for myViewBoard](https://www.viewsonic.com/solution/kb/en_US/other-resources-1/casting-solutions-myviewboard)
    * [EXE vs. MSI for Whiteboard for Windows installation](https://www.viewsonic.com/solution/kb/en_US/other-resources-1/exe-vs-msi-wb-windows-install)
    * [myviewboard.com release history](https://www.viewsonic.com/solution/kb/en_US/other-resources-1/myviewboard-release-history)
    * [NFC management](https://www.viewsonic.com/solution/kb/en_US/vs-entity-management/nfc-management)


#### Was this article helpful?
[](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances) [](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
Print 
# Software instances
In the **Software Instances** dashboard, configure [myViewBoard Whiteboard](https://www.viewsonic.com/solution/kb/es_ES/getting-started-whiteboard/overview-whiteboard) settings for users in your entity. This is a convenient way for admin to ensure the application across devices all meet the school's requirements.
## What is a software instance?
A software instance is any installation of myViewBoard Whiteboard (for Windows, Android, and iOS versions) that can be configured with specific settings by IT admin. If the Whiteboard software is deleted and reinstalled, it will count as a separate instance as it requires enrollment as an instance again (requiring a new name and ID).
[Delete](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
**ENROLLMENT AND WINDOWS VERSION OF myViewBoard WHITEBOARD**
Whiteboard for Windows instances can currently only be enrolled via mass deployment. Though mass deployment methods are not within the scope of this page, [view the installing instances instructions](https://www.viewsonic.com/solution/kb/entity-management-1/myviewboard-deployment#myviewboard-whiteboard-msi-installation-windows-0) section for more info.
## How to enroll software instances
If instances of the Windows version of Whiteboard are [installed using MSI Command Prompt or Group Policy (or similar)](https://www.viewsonic.com/solution/kb/entity-management-1/myviewboard-deployment#command-prompt-to-install-myviewboard-windows-1), and the organization is correctly entered to match that of your entity, enrollment is automatic and no other manual action is required.
For entities who use the Android version of Whiteboard on ViewBoards, enrollment is automatically completed by [adding devices to Manager](https://www.viewsonic.com/solution/kb/getting-started/adding-devices).
Users who installed the Android or iOS version of Whiteboard onto their device can enroll the software instance of Whiteboard after opening it and viewing **Settings >**
[Delete](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
**MAKE SURE TO USE YOUR ENTITY ACCOUNT**
When enrolling instances of Whiteboard (for Android and iOS), make sure to use your myViewBoard email within your entity domain. This will ensure the software instance is automatically registered to that entity and will appear in Entity Management. Any user email address that is registered in the entity user list can enroll the software.
### Methods of enrolling (Android and iOS versions)
Add devices to Manager (IFP Android-only)
This method is only possible on the Android version of Whiteboard installed on ViewBoard IFPs. By [adding a ViewBoard device to Manager](https://www.viewsonic.com/solution/kb/getting-started/adding-devices), the instance of Whiteboard installed on the IFP will automatically be enrolled the next time Whiteboard is launched.
Please note, the first time you launch Whiteboard, you may see the option to enroll your Whiteboard with a form or QR code (see below methods). Restart Whiteboard to see automatic enrollment take effect.
**MANAGER AGENT MUST BE UP TO DATE**
For Whiteboard to successfully enroll into your entity, the Manager agent app on the IFP must be updated to v1.37.3 or later.
**WHITEBOARD NOT ENROLLING?**
If your Manager is up to date, but you do not see your instance added to Software Instances, try clearing Whiteboard app data and cache. Then, restart Whiteboard.
If this doesn't work, you may have to factory reset the device.
Whiteboard Enrollment Form (Android and iOS)
  1. Install Whiteboard onto the device.
  2. Open the software and sign in with your myViewBoard account.
  3. Press 
  4. Press 
  5. Press **Enroll Software Instance under Entity**.
  6. The following are required to complete the Whiteboard Enrollment Form:
     * Whiteboard name
     * myViewBoard email address
  7. After inputting the email address, await detection of the corresponding entity.
  8. A prompt should appear informing you of successful enrollment.


An instance name and a valid myViewBoard entity account are required to complete the enrollment form. 
Whiteboard Enrollment via QR Code (Android and iOS)
This method requires myViewBoard Companion app. To learn the process, [view the Companion app Whiteboard enrollment page](https://www.viewsonic.com/solution/kb/it-support-companion/whiteboard-enrollment).
Activator APK (Android-only)
For non-ViewBoard Android devices, such as Chromebooks, users can enroll Whiteboard through the above form or QR code methods.
Additionally, if users prefer to make enrollment automatic on affected devices, an Activator APK is required. 
You must request an entity-specific Activator APK from your local sales representative or from our support team.
Once received, install the APK onto your desired devices. After doing so, the next time Whiteboard is launched on those devices, those instances will automatically be enrolled to your entity.
[Delete](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
**NOTE ON WHITEBOARD NAME**
Currently, the only way to set a Whiteboard Name for Android and iOS instances is through either the enrollment form or QR code enrollment. When editing the Whiteboard name in the Software Instances console, the name will not update in enrolled Whiteboard app.
### MSI file installation (Windows version)
Whiteboard for Windows is installed from an MSI file. For the purposes of enrollment, Whiteboard can be installed through command prompt.
To learn more, [view the MSI file installation page](https://www.viewsonic.com/solution/kb/entity-management-1/myviewboard-deployment#myviewboard-whiteboard-msi-installation-windows-0).
## Access the Software Instances console
After enrolling your desired instances, they will be viewable in the Software Instances console.
  1. Sign in to 
  2. Open Entity Management.
  3. On the left-side menu, enter **Software Instances**.


## Software Instances console overview
Primary sections of Software Instances console highlighted (left-to-right): Left-side menu, main toolbar, instances list, instance quick info panel.
Left-side menu
**Entity** | Identifies which entity's instances you are viewing.  
---|---  
**All Instances** | View all instances under this entity.  
**Groups** | View all instance groups that have been created under this entity.  
**Templates** | View all templates that have been created under this entity.  
Main toolbar
**Edit instance** | Update the specific configuration for selected instances.  
---|---  
**Add to group** | Move selected instances into an instance group.  
**Delete instance** | Remove instance enrollment from this entity.  
**Filter by OS** | Filter instance list by OS.  
Instances list
**Checkboxes** | When an instance row's box is checked, the main toolbar will fill with options.  
---|---  
**Instance ID** | Identifies a unique instance. Automatically generated when the instance is enrolled.  
**Whiteboard name** | Whiteboard nickname given when the instance is enrolled. Can be edited by pressing   
**Last sign-in user** | The user that last signed in to this instance.  
**OS** | Identifies the OS version of this instance.  
**Version** | Identifies the version number of this instance.  
**IP Address** | Identifies the IP Address last detected for this instance.  
**Template** | Identifies the assigned template of this instance.  
Will appear empty if this instance does not have an assigned template.  
Instance quick view
This panel displays the current configurations for the currently selected instance. To view the quick info for a given instance, simply click the row of the desired instance. You know you will have selected an instance successfully because the panel should no longer be grayed out.
Editing these configurations can be done by selecting a desired instance and pressing 
## Identifying an instance
When viewing your entity's list of instances, verify the instance with the **Instance ID** and **Whiteboard Name**.
Windows settings pictured over Software Instances page with Whiteboard Name and Instance ID highlighted.
## Configure an instance's settings
  1. On an instance list view, check the box for all desired instances.
  2. On the main toolbar, press 
  3. Configure desired settings. (See breakdown below.)
  4. (Optional) Press **+ Save current settings as a template** to save this configuration as a template for later use.
  5. When ready, press **OK** to update instance settings.


Settings pop-up within Software Instances.
[Delete](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
**PERSONALIZED WHITEBOARD SETTINGS VS SOFTWARE INSTANCE SETTINGS**
Though [entity users can personalize their Whiteboard settings](https://www.viewsonic.com/solution/kb/en_US/account-settings/followme-settings), the configurations set by admin within Software Instances will override corresponding personalized settings.
Instance settings options
**Template** | Identifies whether the instance you are viewing is configured following a template. Press   
---|---  
**Check for update** | Sets whether users will automatically be notified of new versions of myViewBoard Whiteboard on launching the application.  
**Local save** | Sets whether users are permitted to save to the local storage on the device where the instance is installed.  
**Sign in function** | Sets whether this instance permits users to sign in or not.  
**Embedded Browser** | Hides or makes available the Embedded Browser   
**Allow stay signed in** | Sets whether users will have the option to keep themselves signed in, even after closing the application.  
**Auto sign out time (Windows-only)** | Sets a maximum duration, after which a user will automatically be signed out.  
**Note:**_Allow stay signed in_ overrides this option.  
**Save current settings as a template** | Press this button to save the current configuration as a template. The template will become available in the left-side menu, and it will be selectable in the _Template_ section of this settings window.  
[Delete](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances)
**GROUPS FOR MORE CONVENIENT CONFIGURATION**
When setting up your entity and its instances, we recommend you group instances based on instance usage expectation on a given device. For example,
  * Do you need to ensure users are auto signed out because multiple teachers use the device within a given day? Configure _auto sign out time_ to 1 hour.
  * Or does one teacher typically use the device? Configure _allow stay signed in_ to ON.
  * Is the Whiteboard instance fulfilling more of a demo purpose? Configure _sign in function_ to OFF.


These are just a few scenarios. Set up groups to make this process more efficient, as well as easier to remember at times of needing to reconfigure devices and instances. 
### Templates
There are two general ways of applying a template to instances.
  1. On an instance list, select from a list of previously created templates by pressing 


List of templates when configuring instance settings.
  1. On a template page, view devices currently applied with this template and have the option to add more:


  
Template page with Apply template to devices pop-up open. List of devices is available to select from to apply the currently viewed template. Devices which are using this template are on the right-side panel.    

### Setting a default template
Additionally, any template created can be **set as default**. By doing so, any new instance added to your entity will be updated with this template's configuration. In this way, no action is required to change new instances' settings configurations unless you would like for those instances to follow a different configuration.
To set a template as default, simply press the **Set as default** button when on the page of your desired template.
The current default template will be indicated by 
View of a template with the **Set as default** button highlighted.
### Reset an instance to default
Additionally, you also have the ability to reset instances configured to a template's settings to the default template configuration.
To do so, go to the template with your desired instance(s). On the right-side panel displaying the list of instances configured to this template, press 
You also have the option to check the box for multiple instances and press the **reset button** that appears below.
Instance list with options to reset a single instance or multiple instances highlighted.   

## Learn more
YouTube video player   
https://www.youtube.com/watch?v=yqGVeI8bjOg
  

« Previous 
Next »
Contents
[What is a software instance? ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#what-is-a-software-instance-0) [How to enroll software instances ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#how-to-enroll-software-instances-1) [Methods of enrolling (Android and iOS versions) ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#methods-of-enrolling-android-and-ios-versions-2) [MSI file installation (Windows version) ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#msi-file-installation-windows-version-3) [Access the Software Instances console ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#access-the-software-instances-console-4) [Software Instances console overview ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#software-instances-console-overview-5) [Identifying an instance ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#identifying-an-instance-6) [Configure an instance's settings ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#configure-an-instances-settings-7) [Templates ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#templates-8) [Setting a default template ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#setting-a-default-template-9) [Reset an instance to default ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#reset-an-instance-to-default-10) [Learn more ](https://www.viewsonic.com/solution/kb/entity-management-1/software-instances#learn-more-11)
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
Sat Jan 03 2026 21:39:56 GMT+0800 (Taiwan Standard Time)
Do you have questions?   
We are here to answer. 😊
