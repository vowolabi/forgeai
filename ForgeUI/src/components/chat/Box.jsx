import { useState, useEffect } from 'react';
import clsx from 'clsx';

export default function Box({who, type, data}) {
    return (
        <div className={clsx("w-100 min-h-10", {
            "bg-gray-800 text-gray-500 text-sm": who === 'user',
            "bg-gray-700 text-white text-sm": who === 'forge'
        })}>
            <div className="p-2">{who === 'user' ? "You" : "ForgeAI"}</div>
            { type === "audio" ? (
                <div className="p-2">
                    <audio controls="controls" autobuffer="autobuffer">
                        <source src={'data:audio/mp3;'+data} />
                    </audio>
                </div>
            ): null }
            { type === "image" ? (
                <div className="p-2">
                    <img src={'data:image/png;'+data}  width="400"></img>
                </div>
            ): null }
            { type === "video" ? (
                <div className="p-2">
                    <video width="400" controls>
                        <source src={'data:video/mp4;'+data} />
                    </video>
                </div>
            ): null }
            { type === "text" ? (
                <div className="p-2">{data}</div>
            ): null }
          </div>
    );
  }