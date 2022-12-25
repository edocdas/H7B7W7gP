from msedge.selenium_tools import EdgeOptions, Edge

options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"/usr/bin/microsoft-edge-dev"
options.set_capability("platform", "LINUX")

webdriver_path = r"/your_path/msedgewebdriver"

browser = Edge(options=options, executable_path=webdriver_path)
browser.get("https://www.google.com")