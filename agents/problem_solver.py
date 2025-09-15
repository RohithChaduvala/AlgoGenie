from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client

model_client= get_model_client()

def get_problem_solver_agent():
    problem_solver_agent= AssistantAgent(
        name="DSA_ProblemSolverAgent",
        description="An expert in solving DSA problems",
        model_client=model_client,
        system_message='''
    You are a problem solver agent that is an expert in solving DSA problems.
    You will be working with code executor agent to execute code.
    You will be given a task and you should :
    1. Write code to solve the task. Your code shall be only in Python.
    At the beginning of the response , you have to specify your plan to solve the task.
    Then you have to write the code in a code block.(Python)
    You should write code in a single code block at a time and then pass it to CodeExecutorAgent to execute it.
    make sure you have three test cases for the code you write.
    Once the code is executed and if the same has been done successfully, you have the results.
    In the end once code is executed successfully, you have to say "STOP" to terminate the chat.
    ''')
    return problem_solver_agent
