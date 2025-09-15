import streamlit as st
from teams.dsa_team import get_dsa_team_and_docker
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio

st.title("AlgoGenie - DSA Problem Solver")
st.write("Welcome to AlgoGenie! Your personal DSA problem solver powered by AI. Here you can ask various DSA related questions and get instant solutions.")

task= st.text_input("Enter your DSA problem or question:")

async def run(team, docker, task):
    await start_docker_container(docker)
    async for message in team.run_stream(task=task):
        if isinstance(message, TextMessage):
            msg = message
            print(f"{msg.source}: {msg.content}")
            yield msg
        elif isinstance(message, TaskResult):
            msg = message
            print(f"Stop Reason: {msg.stop_reason}")
            yield msg
    print("Task completed.")
    await stop_docker_container(docker)        

if st.button("Solve"):
    st.write(f"Running the task")
    team, docker= get_dsa_team_and_docker()

    async def collect_messages():
        async for msg in run(team, docker, task):
            if isinstance(msg, TextMessage):
                st.markdown(f"{msg.source}: {msg.content}")
            elif isinstance(msg, TaskResult):
                st.markdown(f"Stop Reason: {msg.stop_reason}")
    asyncio.run(collect_messages())