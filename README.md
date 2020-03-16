# TLOPO-Launcher

#### Features

* Multi-distribution launching
    * Live, Test, QA/Dev (cannot test QA but it should work)
    * Launch all at the same time without redownloading the default launcher
* Portable
    * Can be moved to whatever location of your choice
    * Creates folders in the directory you put it in - so make a folder for it to reside in
* Multi-platform
    * Tested on Windows 10 and Linux (Ubuntu 18.04.4)
    * Likely works on MacOS (cannot test or compile)
* Supports downloads
    * No need for default launcher

#### Planned Features

- GUI
    -[ ] Basic functionality
    -[ ] With option to run in command line
    -[ ] Stylish look
    -[ ] Resolution Scaling
    -[ ] Download progress
    -[ ] Blog posts
    -[ ] Release notes
- Credential remembering
    -[ ] Usernames
    -[ ] Password (This would be a security issue even if handled correctly, so might not)
- Localization Support (Useless? Not sure if the game supports other languages but nice feature anyways)
    -[ ] English localization
- Game settings configuration

#### Known Issues

* Live version appears to get stuck after initial download. Unsure of cause as the actual game binary is what is getting stuck, not my launcher. Will investigate further. Workaround: just relaunch.
* Patching with TLOPO's patch files is non-functional (I'm unsure if this will break things in the future)
* Binary is somewhat large compared to code, bloated w/ unused python modules

##### Note for linux users

You'll have to download the following packages with your distro's package manager:
- libopenal
- libCg
- libCgGl
- libpng12

Make sure tlopo_test is also set to *allow executing*. You can run this command from the terminal to accomplish this:
- sudo chmod +x tlopo_test
