from django import http
from django.views import View
from django.core.cache import caches
from redis.exceptions import RedisError, ConnectionError


import logging
import re


logger = logging.getLogger('django')


def parse_sms(sms_content):
    """
    对短信内容进行解析
    :param sms_content:
    :return:
    """
    pattern = re.compile(r'.*?【(.*?)】.*?验证码.*?(\d{4,6})',re.S)
    result = re.search(pattern,sms_content)
    if result:
        send_name = result.group(1)
        sms_code = result.group(2)
        return send_name,sms_code
    else:
        return False



class SmsMobilePhone(View):
    """
    接受手机短信传来的信息
    """
    def post(self,request):
        sms_content = request.POST.get('content', 0)
        if sms_content == 0:
            return http.JsonResponse({"code": 600, "msg": "接受失败",'sms':sms_content})
        logger.info(f'接受到的短信验证码为：{sms_content}')

        # 进行验证码的解析
        result = parse_sms(sms_content)
        if result:
            sms_cache = caches['SmsMobilePhone']
            send_name,sms_code = result
            logger.info('数据为: %s, %s', send_name, sms_code)
            # 这里假设用 send_name 作为 Key 保存验证码，设置过期时间为 300 秒（5分钟）
            try:
                sms_cache.set(send_name, int(sms_code), timeout=3000)
            except RedisError:
                logging.error('保存redis失败')
            else:
                return http.JsonResponse({"code": 200, "msg": "接收成功", 'sms': sms_content})
        else:
            return http.JsonResponse({"code": 700, "msg": "短信解析失败",'sms':sms_content})
