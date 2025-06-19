from captcha.image import ImageCaptcha
import random
import string

def generate_captcha(width=280, height=90, characters_length=4):
    # 生成随机验证码字符
    characters = ''.join(random.choices(string.ascii_letters + string.digits, k=characters_length))
    
    # 创建验证码图片
    captcha = ImageCaptcha(width=width, height=height)
    
    # 生成验证码图片
    data = captcha.generate(characters)
    
    # 保存验证码图片到文件
    captcha.write(characters, 'captcha.png')
    
    # 返回验证码字符
    return characters

# 调用函数生成验证码
captcha_text = generate_captcha()
print(f"生成的验证码是: {captcha_text}")