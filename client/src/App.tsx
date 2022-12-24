import React, { useState } from 'react';
import './App.css';
import Status from './components/status/Status';
import Select from './components/select/Select';
import Stop from './components/stop/Stop';
import Favourites from './components/favourites/Favourites';
import StatusContext from './store/status-context';

function App() {

  const [isOn, setIsOn] = useState(false);
  
  return (
    <div className="App">
      <StatusContext.Provider value={{isOn: isOn, flipIsOn: () => setIsOn(!isOn), setOn: () => setIsOn(true), setOff: () => setIsOn(false)}}>
        <Status></Status>
        <Stop></Stop>
        <Select></Select>
        <Favourites></Favourites>
      </StatusContext.Provider>
    </div>
  );
}

export default App;
