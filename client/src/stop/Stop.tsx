import React from 'react';
import { SERVER_URL } from '../constants';

const stop = () => fetch(`${SERVER_URL}/stop`, { method: 'POST'})

function Stop() {
  return (
    <div className="Stop">
      <input type="button" value="Stop" onClick={stop}/>
    </div>
  );
}

export default Stop;
