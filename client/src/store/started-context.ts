import React from 'react';

interface IsOnContextProps {
  isOn: boolean;
  flipIsOn: Function;
  setOn: Function;
  setOff: Function;
}

const IsOnContext = React.createContext<IsOnContextProps>({
  isOn: false,
  flipIsOn: () => {},
  setOn: () => {},
  setOff: () => {},
});

export default IsOnContext;