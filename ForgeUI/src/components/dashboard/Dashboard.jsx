import { MdOutlineTextsms } from "react-icons/md";
import { IoMusicalNotes } from "react-icons/io5";
import { FaImage } from "react-icons/fa";
import { FaVideo } from "react-icons/fa";
import { MdOutlineDocumentScanner } from "react-icons/md";
import { useState } from "react";

export function NavItem({setCurrentMode, icon, text, dropdown_items = []}) {
  const [isItemOpen, setItemOpen] = useState(false);
  return (
    <div className="gap-0 group hover:scale-105" >
      <div onClick={() => setItemOpen(!isItemOpen)} className="px-3 flex items-center  gap-3 border-slate-500 border-[1px] rounded-md text-gray-400 cursor-pointer hover:shadow-md hover:text-black duration-200">
        {icon}
        <div>{text}</div>
      </div>
      { isItemOpen && dropdown_items.length !== 0 ? (
      <div className="p-2 mt-1 w-full border-gray-500 border-[1px] rounded-md text-black">
        {dropdown_items.map((value,index) => {
          return (<div key={index} className="pl-2 hover:bg-gray-600 cursor-pointer rounded-sm " onClick={() => {
            setCurrentMode({topic:text});
          }}>{value}</div>)
        })}
      </div>)
      : 
      null}
    </div>
  )
}
export default function Dashboard({setCurrentMode}) {
  return (
    <div className="w-1/5 p-7 h-full bg-neutral-100 flex flex-col gap-y-4 shadow-xl">
      <div className="flex gap-2 w-full flex-col justify-center items-center">
        <img src="better_colored.png" className="w-[45px] h-[45px]"></img>
        <div className="text-black tracking-wide">FORGE AI</div>
      </div>
      <NavItem setCurrentMode={setCurrentMode} icon={<MdOutlineTextsms className="text-gray-400 group-hover:text-black" />} text="Text" dropdown_items={['Chat with ForgeAI']}></NavItem>
      <NavItem setCurrentMode={setCurrentMode} icon={<IoMusicalNotes className="text-gray-400 group-hover:text-black" />} text="Audio" dropdown_items={['Transcription']}></NavItem>
      <NavItem setCurrentMode={setCurrentMode} icon={<FaImage className="text-gray-400 group-hover:text-black" />} text="Image" dropdown_items={['Image Captioning']}></NavItem>
      <NavItem setCurrentMode={setCurrentMode} icon={<FaVideo className="text-gray-400 group-hover:text-black" />} text="Video" dropdown_items={['Video Captioning']}></NavItem>
    </div>
  );
}
