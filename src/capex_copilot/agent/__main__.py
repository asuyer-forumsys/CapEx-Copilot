#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

import argparse
from run_agent import AIAgent


def run_agent(query: str):
    agent = AIAgent(
        model="gpt-5.3-codex",
        quiet_mode=False,
        enabled_toolsets=["rag_retrieval"],
    )

    agent.chat(query)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Document ingester")
    parser.add_argument("query")
    args = parser.parse_args()

    run_agent(args.query)
