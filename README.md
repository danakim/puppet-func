puppet-func
===========

A [Func](https://fedorahosted.org/func/) plugin to control the Puppet agent.

Func is a server orchestration framework that is highly pluggable.

This plugin / module will help Func users control the Puppet agent and Puppet runs throughout their infrastructure.

Installation instructions can be found in the [Func documentation.](https://fedorahosted.org/func/wiki/HowToWriteAndDistributeNewModules)
Basically you have to drop the puppet.py file in /usr/lib/python$version/site-packages/func/minion/modules/ on every box you want this to be available and then restart the Func
agent.
