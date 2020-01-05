import asyncio
import time

async def download_url(url):
    print('start get %s' % url)
    await asyncio.sleep(2)
    print('get %s finished.' % url)

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_url('https:www.baidu.com')) # 阻塞等事件完成之后再向下运行。相当于进程线程的join()方法，或者进线程池的wait()
    print('一共用时：%s' % (time.time() - start_time))