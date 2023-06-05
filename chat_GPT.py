from selenium import webdriver
import time

# 配置 webdriver 路径和浏览器选项
driver_path = "/path/to/chromedriver"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
browser = webdriver.Chrome(executable_path=driver_path, options=options)

# 进入京东网站并搜索商品
browser.get('https://www.jd.com/')
search_box = browser.find_element_by_id('key')
search_box.send_keys('苹果手机')  # 搜索关键词
search_button = browser.find_element_by_class_name('button')
search_button.click()
time.sleep(2)

# 进入商品详情页并添加至购物车
product_link = browser.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a')
product_link.click()
add_cart_button = browser.find_element_by_xpath('//*[@id="InitCartUrl"]')
add_cart_button.click()
time.sleep(2)

# 进入购物车页面并提交订单
cart_link = browser.find_element_by_partial_link_text('去购物车结算')
cart_link.click()
submit_order_button = browser.find_element_by_id('order-submit')
submit_order_button.click()

# 关闭浏览器
browser.quit()





