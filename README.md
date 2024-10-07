# Web3 Development Workshop

This repository contains the code and documentation for a Web3 Development Workshop that demonstrates how to integrate AWS cloud services with a decentralized application (dApp). The project highlights the use of smart contracts, AWS Lambda, API Gateway, and other AWS services to create a scalable Web3 solution.

## Overview

The goal of this workshop is to showcase how to build, deploy, and integrate a decentralized application (dApp) with AWS infrastructure. By combining blockchain technology with cloud services, we can leverage the scalability and security of AWS to manage a decentralized environment.

### Key Objectives:
- Develop and deploy Solidity smart contracts.
- Use AWS services to integrate blockchain data and events.
- Store decentralized application data using IPFS and AWS S3.
- Automate workflows using AWS Lambda and API Gateway.

## Project Structure

The repository is organized as follows:

- **build/**: Contains compiled artifacts of the smart contracts, including ABI (Application Binary Interface) files necessary for interacting with the contracts.
  
- **docs/**: Documentation related to the project, including architecture diagrams and detailed explanations of how the system is set up.
  
- **script/**: Scripts that facilitate deployment and interaction with the smart contracts via Truffle or other deployment tools.

- **smart_contracts/**: The Solidity smart contracts that manage the core functionality of the dApp. These contracts handle key blockchain interactions, such as token minting and transfers.

- **tests/**: Test files for ensuring that the smart contracts behave as expected. These tests can be run to validate the functionality of the contracts before deployment.

- **truffleApp/**: The main Truffle project directory, containing configuration files for deploying the smart contracts and managing interactions with the blockchain network.

## Architecture

![Architecture Diagram](https://github.com/Gojaman/web3-development-aws/blob/main/docs/architecture-diagram.png)

The above diagram outlines the architecture used for this project. Key components include:
- **AWS Lambda**: Handles backend logic and integration with the blockchain.
- **Amazon API Gateway**: Acts as an entry point for API requests to interact with the smart contracts.
- **Amazon Managed Blockchain**: Provides the blockchain infrastructure for secure and scalable smart contract deployment.
- **IPFS**: Decentralized storage for data that needs to remain immutable and distributed.
- **Amazon S3**: Serves as additional storage for off-chain data related to the dApp.

## Smart Contracts

The smart contracts for this project are written in **Solidity** and are responsible for managing the core functionality of the dApp. These contracts are deployed on the Ethereum blockchain, but the architecture can be adapted to other chains.

### Key Contracts:

- **Token.sol**: 
  - Implements a basic ERC-20 token that users can mint, transfer, and manage. The contract is integrated with AWS to trigger off-chain events based on certain blockchain transactions.
  - **Functions**:
    - `mint()`: Allows authorized users to mint new tokens.
    - `transfer()`: Facilitates token transfers between users.

### Deployment Instructions:

1. **Compile the Smart Contract**:
   - Open [Remix](https://remix.ethereum.org) and load `Token.sol`.
   - Go to the **Solidity Compiler** tab and select version `0.8.26` (or the version matching your contract).
   - Click **Compile Token.sol**.

2. **Deploy the Smart Contract**:
   - In the **Deploy & Run Transactions** tab, select the environment (`Injected Web3` for MetaMask or other wallet integrations).
   - Set the contract parameters (if applicable) and click **Deploy**.
   - Confirm the transaction in your wallet (MetaMask, etc.).

3. **Interaction with the Contract**:
   - After deployment, you can interact with the contract through Remix or by calling functions via the frontend, once it’s developed.

## AWS Integration

The AWS integration allows the dApp to scale and automate backend processes without relying solely on the blockchain. The **aws_integration/** folder contains Lambda functions and configuration files for API Gateway.

### Key AWS Components:
- **AWS Lambda**: Processes off-chain events triggered by smart contract interactions.
- **API Gateway**: Acts as the interface for making API calls to AWS services from the blockchain.
- **Amazon Managed Blockchain**: Provides a secure environment for deploying and managing smart contracts.

### Setup Instructions:

1. **Configure AWS Lambda**:
   - Deploy the Lambda function provided in the `aws_integration/lambda_function.py` file.
   - Ensure it is set up to trigger based on smart contract events or API Gateway calls.

2. **Set Up API Gateway**:
   - Create an API in Amazon API Gateway that connects to your Lambda function.
   - Configure necessary endpoints to interact with the smart contracts and pass data between the blockchain and AWS.

## Frontend

The frontend will be responsible for providing an interface for users to interact with the dApp. It will use web3.js (or ethers.js) to interact with the smart contracts and AWS API Gateway for backend interactions.

Currently, this section is a placeholder for future development. The frontend files will be uploaded once the user interface is implemented.

## Prerequisites

Before you get started, ensure that you have the following:

- [Node.js](https://nodejs.org/en/) for managing dependencies.
- An [AWS Account](https://aws.amazon.com/free/) to set up the required AWS services.
- [MetaMask](https://metamask.io/) or another web3 wallet to interact with the Ethereum network.
- [Remix IDE](https://remix.ethereum.org) for compiling and deploying smart contracts.

## Getting Started

To set up this project on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Gojaman/web3-development-aws.git
   cd web3-development-aws
