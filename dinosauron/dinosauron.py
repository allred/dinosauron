import subprocess

class Dinosauron:
    def __init__(self):
        pass

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
