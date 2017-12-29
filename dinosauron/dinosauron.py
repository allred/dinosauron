import asyncio
import subprocess
from collections import defaultdict

class Dinosauron:
    def __init__(self):
        self.results_dig = defaultdict(lambda: "")

    def dig_mdns(self, address):
        """
           multicast dns query
           note that the initial run of parallel may hang for a "citation" prompt
           parallel -j0 --tag dig +time=1 +short -x {} @224.0.0.251 -p 5353 ::: 192.168.0.1 192.168.0.103
        """
        proc = subprocess.Popen(["dig", "+time=1", "+short", "-x", address, "@224.0.0.251", "-p", "5353"], stdout=subprocess.PIPE)
        (out, err) = proc.communicate()
        if proc.returncode == 0:
            return out
        else:
            return None

    async def diggy(self, address):
        result = self.dig_mdns(address)
        self.results_dig[address] = result
        return result

    def dig_async(self, addresses):
        tasks = []
        ioloop = asyncio.get_event_loop()
        for a in addresses:
            tasks.append(ioloop.create_task(self.diggy(a)))
        wait_tasks = asyncio.wait(tasks)
        ioloop.run_until_complete(wait_tasks)
        ioloop.close()
        return self.results_dig
