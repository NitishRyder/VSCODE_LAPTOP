import React from "react";
import "./TextField.css"

function TextField(){
    return (
        <div>
            <label htmlFor="name" id="name">Enter Name:</label><br />
            <input type="text" id="input" />
        </div>
    );
}

export default TextField;