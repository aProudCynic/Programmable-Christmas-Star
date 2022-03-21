import React, { useState } from 'react';
import './App.css';
import IsOn from './components/is_on/IsOn';
import Select from './components/select/Select';
import Stop from './components/stop/Stop';
import IsOnContext from './store/started-context';

function App() {

  const [isOn, setIsOn] = useState(false);
  
  return (
    <div className="App">
      <IsOnContext.Provider value={{isOn: isOn, flipIsOn: () => setIsOn(!isOn), setOn: () => setIsOn(true), setOff: () => setIsOn(false)}}>
        <IsOn></IsOn>
        <Stop></Stop>
        <Select></Select>
      </IsOnContext.Provider>
    </div>
  );
}

export default App;
