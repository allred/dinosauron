from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from time import sleep

def do_scan(targets, options):
    parsed = None
    nmproc = NmapProcess(targets, options)
    rc = nmproc.run()
    if rc != 0:
        print("nmap scan failed: {0}".format(nmproc.stderr))
    print(type(nmproc.stdout))

    try:
        parsed = NmapParser.parse(nmproc.stdout)
    except:
        print("Exception raised while parsing scan: {0}".format(e.msg))
    return parsed

def print_scan(nmap_report):
    print("Starting Nmap {0} at {1}".format(
        nmap_report.version,
        nmap_report.started,
    ))
    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        print("Nmap scan report for {0} ({1})".format(
            tmp_host,
            host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)
    print(nmap_report.summary)

def scan_async(targets, options):
    nmap_proc = NmapProcess(targets, options)
    rc = nmap_proc.run_background()
    while nmap_proc.is_running():
        print("scanning {0}: ETC: {1} DONE: {2}% {3}".format(
            targets,
            nmap_proc.etc,
            nmap_proc.progress,
            nmap_proc.rc,
        ))
        sleep(2)
    try:
        parsed = NmapParser.parse(nmap_proc.stdout)
    except:
        print("Exception raised while parsing scan: {0}".format(e.msg))
    return parsed

def background_proc(targets, options, event_callback=None):
    nmap_proc = NmapProcess(targets, options, event_callback)
    nmap_proc.run_background()
    return nmap_proc


def scan_many(targets, options):
    still_running = True 
    results = []
    for target in targets:
        results.append(background_proc(target, options))
    while still_running:
        count_running = 0
        for process in results:
            if process.is_running():
                count_running += 1
        if count_running == 0:
            still_running = False
        else:
            print("{} running".format(count_running))
            sleep(1)
    for result in results:
        parsed = NmapParser.parse(result.stdout) 
        print_scan(parsed)

if __name__ == "__main__":
    scan_many(["127.0.0.1", "scanme.nmap.org"], "-sV")

#print("rc: {0} output: {1}".format(nmap_proc.rc, nmap_proc.summary))

#nm = NmapProcess("scanme.nmap.org", options="-sV")
#rc = nm.run()
#if nm.rc == 0:
    #print(nm.stdout)
#    print(nm)
#else:
#    print(nm.stderr)
