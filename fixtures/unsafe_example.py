# TEST FIXTURE ONLY. Deliberately unsafe patterns. Never import, run, or deploy.
import subprocess


def unsafe_expression(user_input):
    return eval(user_input)


def unsafe_command(user_input):
    return subprocess.check_output(user_input, shell=True, text=True)
