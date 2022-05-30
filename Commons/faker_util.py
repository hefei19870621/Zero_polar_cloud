"""
@Filename:  Commons/faker_util
@Author:    何飞
@Time:      2022/5/19 9:55
"""
from faker import Faker


#模拟生成数据
'''
    简体中文：zh_CN
    繁体中文：zh_TW
    美国英文：en_US
    英国英文：en_GB
    德文：de_DE
    日文：ja_JP
    韩文：ko_KR
    法文：fr_FR
'''
faker=Faker(locale="zh_CN")

# print('image url:',faker.image_url())
# print('explorer:',faker.internet_explorer())
# print('IPv4:',faker.ipv4())
# print('IPv6:',faker.ipv6())
# print('IPv4 private:',faker.ipv4_private())
# print('IPv4 public:',faker.ipv4_public())
print("姓名：",faker.name())
print("身份证号：",faker.ssn(min_age=18, max_age=90))
print("手机号：",faker.phone_number())
print("详细地址：",faker.address())
print("公司名：",faker.company())
print("邮箱：",faker.ascii_free_email())
print("省：",faker.province())
print("市：",faker.city_name())
print("邮编：",faker.postcode())
print("路：",faker.street_name())
print("座：",faker.street_address())
print("颜色：",faker.hex_color())



