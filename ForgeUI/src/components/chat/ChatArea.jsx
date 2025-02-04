import ChatboxArea from "./ChatboxArea";
import { useState, useEffect } from 'react';
import axios from 'axios';
import clsx from 'clsx';
import Box from "./Box";

const URL = "https://forgeapp.azurewebsites.net/api/run?";
const HISTORY_URL = "https://forgeapp.azurewebsites.net/api/history";

async function getHistory() {
  try {
    const response = await axios.get(HISTORY_URL);
    return response.data;
  } catch (error) {
    console.error("There was an error calling the Azure Function:", error);
  }
}

async function callAzureFunction(url, data) {
  try {
    const response = await axios.post(url, data);
    return response.data;
  } catch (error) {
    console.error("There was an error calling the Azure Function:", error);
  }
}

export default function ChatArea({ state }) {
  const [messageHistory, setMessageHistory] = useState([]);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    if (!mounted) {
      getHistory().then((history) => {
        setMessageHistory(history);
      });
      setMounted(true);
    }
  }, [mounted]);

  const messages = messageHistory.map((message, index) => (
    <div key={index}>
      <Box who="user" type={message.type} data={typeof message.user === 'object' ? JSON.stringify(message.user) : message.user} />
      <Box who="forge" type={message.type_response} data={typeof message.response === 'object' ? JSON.stringify(message.response) : message.response} />
    </div>
  ));

  function handleText(e) {
    e.preventDefault();
    const value = e.target[0].value;
    const tempMessage = { type: "text", user: value, type_response: "text", response: "..." };
    setMessageHistory((prevMessages) => [...prevMessages, tempMessage]);

    callAzureFunction(URL, { action: 'text2text', data: 'data:text/txt;' + value }).then(
      (response) => {
        const finalMessage = { type: "text", user: value, type_response: "text", response: typeof response === 'object' ? JSON.stringify(response) : response };
        setMessageHistory((prevMessages) => [...prevMessages, finalMessage]);
      }
    );

    e.target[0].value = "";
  }

  function handleFile(e, action) {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = function () {
      const result = reader.result;
      const tempMessage = { type: action, user: result, type_response: "text", response: "..." };
      setMessageHistory((prevMessages) => [...prevMessages, tempMessage]);

      callAzureFunction(URL, { action: action + '2text', data: result }).then(
        (response) => {
          const finalMessage = { type: action, user: result, type_response: "text", response: typeof response === 'object' ? JSON.stringify(response) : response };
          setMessageHistory((prevMessages) => [...prevMessages, finalMessage]);
        }
      );
    };

    reader.readAsDataURL(file);
  }

  return (
    <div className="w-4/5 bg-gray-200">
      <div className="w-100 h-4/5 bg-slate-600 overflow-y-scroll">
        {messages}
      </div>
      <ChatboxArea
        state={state}
        onTextLoad={handleText}
        onAudioLoad={(e) => handleFile(e, 'audio')}
        onImageLoad={(e) => handleFile(e, 'image')}
        onVideoLoad={(e) => handleFile(e, 'video')}
      />
    </div>
  );
}
