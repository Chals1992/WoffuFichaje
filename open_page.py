Run python auto_fichar.py
  
Traceback (most recent call last):
  File "auto_fichar.py", line 24, in <module>
    driver = webdriver.Chrome(service=service, options=options)
  File "/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/selenium/webdriver/chrome/webdriver.py", line 45, in __init__
    super().__init__(
  File "/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/selenium/webdriver/chromium/webdriver.py", line 66, in __init__
    super().__init__(command_executor=executor, options=options)
  File "/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 212, in __init__
    self.start_session(capabilities)
  File "/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 299, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
  File "/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 354, in execute
    self.error_handler.check_response(response)
  File "/opt/hostedtoolcache/Python/3.8.18/x64/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 229, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: Chrome failed to start: exited abnormally.
  (unknown error: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
Stacktrace:
#0 0x558504df14e3 <unknown>
#1 0x558504b20c76 <unknown>
#2 0x558504b49d78 <unknown>
#3 0x558504b46029 <unknown>
#4 0x558504b84ccc <unknown>
#5 0x558504b8447f <unknown>
#6 0x558504b7bde3 <unknown>
#7 0x558504b512dd <unknown>
#8 0x558504b5234e <unknown>
#9 0x558504db13e4 <unknown>
#10 0x558504db53d7 <unknown>
#11 0x558504dbfb20 <unknown>
#12 0x558504db6023 <unknown>
#13 0x558504d841aa <unknown>
#14 0x558504dda6b8 <unknown>
#15 0x558504dda847 <unknown>
#16 0x558504dea243 <unknown>
#17 0x7f5c0aa94ac3 <unknown>
Error: Process completed with exit code 1.
