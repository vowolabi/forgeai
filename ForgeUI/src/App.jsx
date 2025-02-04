import { useState } from "react";
import ChatArea from "./components/chat/ChatArea";
import Dashboard from "./components/dashboard/Dashboard";

function App() {
  const [currentMode, setCurrentMode] = useState({topic:"Text"});
  
  return (
    <div className='flex w-100 h-screen'>
      <Dashboard setCurrentMode={setCurrentMode} ></Dashboard>
      <ChatArea state={currentMode}></ChatArea>
    </div>
  );
}

export default App;
