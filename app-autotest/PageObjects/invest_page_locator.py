

# 标链接
bid_link_locator = "//a//*[text()='%s']"

# 投标金额输入框
bid_investinput_locator = "//*[text()='%s']//ancestor::div[@class='title']//following-sibling::div[@class='body']//input[@class='form-control invest-unit-investinput']"

# 投标按钮
bid_button_locator = "//*[text()='%s']//ancestor::div[@class='title']//following-sibling::div[@class='body']//button"

# 弹出框
bid_layer_locator = "//div[@id='layui-layer1']"

# 投资成功确认框
bid_invest_sucess_confirm_button_locator = "//*[@id='layui-layer1']//button[text()='查看并激活']"

# 投资失败确认框
bid_invest_fail_confirm_button_locator = "//*[@id='layui-layer1']//a[@class='layui-layer-btn0']"

# 投资失败确认框提示文字
bid_invest_fail_confirm_text_locator = "//*[@id='layui-layer1']//div[@class='text-center']"