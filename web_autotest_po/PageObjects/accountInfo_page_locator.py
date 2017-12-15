# 蜂群链接
fengqun_link_locator = "//a[text()='蜂群/公社']"

# 投资项目
investment_record_locator = "//div[text()='投资项目']"

# 交易记录table
deal_mange_tab_locator = "//div[@class='deal_manage_list' and contains(@style,'display: block')]//table"

# 根据标明和投资时间查找对应的投资记录链接
investment_link_locator = "//div[text()='%s']//following-sibling::div[text()='%s']//parent::td//following-sibling::td//div//a[text()='%s']"

