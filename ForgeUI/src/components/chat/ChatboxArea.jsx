import { FaPaperclip } from "react-icons/fa6";
import { FaPhotoVideo, FaImage } from "react-icons/fa";

export default function ChatboxArea({state, onTextLoad, onAudioLoad, onImageLoad, onVideoLoad}) {
  function insertInputType(state) {
    if (state.topic === "Text") {
      return (
        <input className="w-[400px] h-10 bg-gray-950 text-white border-white border-2 rounded-lg" type="text"></input>
      )
    }
    else if (state.topic === "Audio") {
      return (
      <div className="w-10 h-10 bg-gray-800 flex items-center justify-center hover:bg-slate-500 rounded-lg">          
        <input type="file" accept="audio/*" onChange={onAudioLoad} className="w-full h-full opacity-0"></input>
        <FaPaperclip className="pointer-events-none absolute text-center text-white"></FaPaperclip>
      </div>
      )
    }
    else if (state.topic === "Image") {
      return (
        <div className="w-10 h-10 bg-gray-800 flex items-center justify-center hover:bg-slate-500 rounded-lg">          
          <input type="file" accept="image/*" onChange={onImageLoad} className="w-full h-full opacity-0"></input>
          <FaImage className="pointer-events-none absolute text-center text-white"></FaImage>
        </div>
        )
    }
    else if (state.topic === "Video") {
      return (
        <div className="w-10 h-10 bg-gray-800 flex items-center justify-center hover:bg-slate-500 rounded-lg">          
          <input type="file" accept="video/*" onChange={onVideoLoad} className="w-full h-full opacity-0"></input>
          <FaPhotoVideo className="pointer-events-none absolute text-center text-white"></FaPhotoVideo>
        </div>
        )
    }
  }
  return (
    <div className="w-100 h-1/5 bg-gray-950 flex items-center justify-center">
      <form onSubmit={onTextLoad} className="flex">
        { insertInputType(state)}

        {/* <input type="file" accept="image/*" onChange={onImageLoad}></input> */}
      </form>
   </div>
  );
}
