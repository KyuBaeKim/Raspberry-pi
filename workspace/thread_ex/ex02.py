import threading, requests, time

class HtmlGetter(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        # self.daemon = True  # -> main thread가 종료할 떄 같이 종료 된다.

    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), resp.text )
t = HtmlGetter('https://google.com')
t.start()
# t.run()


print("### End ###")