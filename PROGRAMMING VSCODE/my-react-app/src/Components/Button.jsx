import React from 'react';
import './Button.css'

function Button(){
    let count = 0;

    const handleClick = () => {
        if(count<3){
            count++;
            console.log(`Hi you clicked me ${count} time/s`)
        }
        else{
            console.log(`Stop clicking me!`);
        }
        console.log("OUTCH!");
    };

return <div>
<button onClick={handleClick} id='button'>CLICK HERE</button>
</div>
}
export default Button;
