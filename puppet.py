import func_module
import subprocess
import os
import signal

class Puppetctl(func_module.FuncModule):
    version = "0.0.1"
    api_version = "0.0.1"
    description = "A module to control the puppet agent"

    # Find puppet agent's pid
    def process_pid(self):
        if os.path.exists('/var/run/agent.pid'):
            f = open('/var/run/agent.pid', 'r')
            pid_no = f.read()
            return (pid_no)

    def run(self):
        """
        Trigger a one time puppet agent run
        """
        pid = self.process_pid()
        if pid:
            pid_int = int(pid)
            os.kill(pid_int, signal.SIGUSR1)
            return "Puppet run triggered."
        else:
            proc = subprocess.Popen('puppet agent --onetime --ignorecache --no-usecacheonfailure --no-splay --daemonize', stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            output, errors = proc.communicate()
            return (proc.returncode, errors)

    def start(self):
    # TODO: Find a more portable way of starting the agent
        """
        Start the agent
        """
        pid = self.process_pid()
        if pid:
            return "Agent is already running!"
        else:
            proc = subprocess.Popen('/etc/init.d/puppet start', stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            output, errors = proc.communicate()
            return (proc.returncode, errors)

    def stop(self):
        """
        Stop the agent
        """
        pid = self.process_pid()
        if pid:
            pid_int = int(pid)
            os.kill(pid_int, signal.SIGTERM)
            return "Puppet stopped."
        else:
            return "Agent already stopped!"

    def restart(self):
        """
        Restart the agent
        """
        pid = self.process_pid()
        if pid:
            pid_int = int(pid)
            os.kill(pid_int, signal.SIGHUP)
            return "Puppet restarted."
        else:
            self.start()
