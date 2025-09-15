from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_executor import get_docker_executor

def get_code_executor_agent():
    
    docker= get_docker_executor()
    code_executor_agent = CodeExecutorAgent(
            name="CodeExecutorAgent",
            system_message='''
        you are the code executor agent. you monitor the code written by problem solver agent and tell if any mistake is done. if everything is fine tell that the code is correct.
    ''',
            code_executor=docker)
    return code_executor_agent, docker