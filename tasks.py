from invoke import task

# commands for doing different things. 
# If poetry is installed and properly initiated these can be used 
# with syntax: poetry run invoke [command]

@task
def start(ctx):
    ctx.run("python3 src/launch.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage report -m; coverage html") 

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def performance(ctx):
    ctx.run("python3 src/performance.py")
