import asyncio
import time
import pytest

async def download_url(url):
    print('start get %s' % url)
    await asyncio.sleep(2)
    print('get %s finished.' % url)

def test_download_url(url):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_url(url)) # 阻塞等事件完成之后再向下运行。相当于进程线程的join()方法，或者进线程池的wait()
    print('一共用时：%s' % (time.time() - start_time))

if __name__ == '__main__':
    test_download_url('https:www.baidu.com')