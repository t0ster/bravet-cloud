from kokki import Package

env.include_recipe("ssh")

Package("git-core", action="upgrade")
Package("tmux", action="upgrade")
Package("htop", action="upgrade")
Package("sysstat", action="upgrade")
Package("python")
Package("python-dev")
