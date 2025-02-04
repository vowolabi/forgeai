# React Frontend

## Overview

This React application provides a versatile messaging interface that allows users to send and receive messages in different formats, including text, audio, image, and video. The app includes a dashboard for navigation and a chat area for displaying messages and responses. It interacts with an external API to handle message processing and retrieval.

## Table of Contents

1. [Features](#features)
2. [Architecture](#architecture)
3. [Components](#components)
   - [App](#app)
   - [Dashboard](#dashboard)
   - [NavItem](#navitem)
   - [ChatArea](#chatarea)
   - [ChatboxArea](#chatboxarea)
   - [Box](#box)
4. [API Integration](#api-integration)
5. [Styling](#styling)
6. [Setup and Installation](#setup-and-installation)
7. [Usage](#usage)
8. [Future Improvements](#future-improvements)

## Features

- **Multi-Mode Messaging**: Switch between different messaging modes (Text, Audio, Image, Video).
- **Real-Time Responses**: Receive real-time responses from an API based on the sent messages.
- **History Retrieval**: Fetch and display past messages and responses on application load.
- **Dynamic UI**: Responsive and dynamic user interface using React and Tailwind CSS.
- **File Handling**: Upload and handle various file types for audio, image, and video messages.

## Architecture

The application is structured with a clear separation of concerns, using React functional components and hooks for state management. The architecture consists of a main `App` component that orchestrates the other components, a `Dashboard` for navigation, and a `ChatArea` for message display and interaction.

## Components

### App

The `App` component is the root of the application. It maintains the state of the current mode (Text, Audio, Image, Video) and renders the `Dashboard` and `ChatArea` components.

### Dashboard

The `Dashboard` component allows users to switch between different messaging modes. It contains several `NavItem` components, each representing a different mode. Clicking on a `NavItem` updates the current mode in the `App` component.

### NavItem

The `NavItem` component represents a navigational item in the `Dashboard`. It displays an icon and text for the mode, and optionally, a dropdown list of sub-options. When clicked, it updates the current mode in the parent `Dashboard` component.

### ChatArea

The `ChatArea` component manages and displays the message history. It fetches message history from an API on mount and provides methods for handling new messages and file uploads. It renders `Box` components for each message and response.

### ChatboxArea

The `ChatboxArea` component provides input fields for sending messages based on the current mode. It dynamically displays the appropriate input type (text input or file upload) and handles form submissions.

### Box

The `Box` component renders individual messages and responses. It displays the content based on the message type (Text, Audio, Image, Video) and styles the message differently based on the sender (user or API).

## API Integration

The application integrates with an external API for handling message processing and history retrieval. 

- **Message History**: On component mount, the application fetches past messages and responses from the API and displays them in the `ChatArea`.
- **Message Processing**: When a new message is sent, the application calls the API to process the message and receive a response. The response is then displayed in the chat area.

API Endpoints:
- `GET /history`: Retrieves the message history.
- `POST /run`: Processes a new message and returns a response.

## Styling

The application uses Tailwind CSS for styling, providing a modern and responsive design. Key styles include:
- **Dashboard**: A sidebar with navigation items, styled with background colors and hover effects.
- **ChatArea**: A main area for displaying messages, with a scrollable container for the message history.
- **ChatboxArea**: An input area at the bottom for sending new messages, with different input types based on the current mode.
- **Box**: Individual message components, styled differently based on the sender (user or API).

## Setup and Installation

### Prerequisites

- Node.js (v14 or later)
- npm (v6 or later) or yarn (v1 or later)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/react-messaging-app.git
   cd react-messaging-app

   install:
    npm install
    # or
    yarn install

    run:
    npm start
    # or
    yarn start
    ```

## Usage

    Selecting a Mode: Use the sidebar to select the desired messaging mode (Text, Audio, Image, Video).
    Sending a Message: Depending on the selected mode, enter text or upload a file.
    Receiving a Response: The application will display the API's response in the chat area.
    Viewing History: Upon loading, the application fetches and displays past messages and responses.

## Future Improvements

    Enhanced Security: Implement authentication and authorization mechanisms.
    Rich Media Support: Support for additional media types and formats.
    Improved Error Handling: More robust error handling and user feedback.
    Customization Options: Allow users to customize the UI and functionality.