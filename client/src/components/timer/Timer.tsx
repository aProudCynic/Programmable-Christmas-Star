import React, { useState, useRef } from 'react';

const Timer = () => {

    const [timeRemaining, setTimeRemaining] = useState<number>(10);
    const timeRemainingRef = useRef(timeRemaining);
    timeRemainingRef.current = timeRemaining;
    
    const decrementTimeRemaining = () => {
        setInterval(() => {
            console.log(timeRemainingRef, timeRemaining)
            if (timeRemainingRef.current > 0) {
                console.log(`set to ${timeRemainingRef.current - 1}`)
                setTimeRemaining(timeRemainingRef.current - 1)
            } else {
                console.log('clr')
                clearInterval()
            }
        }, 1000);
    }

    return <div>
        {timeRemaining}
        <button onClick={decrementTimeRemaining}>«</button>
    </div>
}
export default Timer;