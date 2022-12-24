import React from 'react';

interface StatusContextProps {
  isOn: boolean;
  flipIsOn: Function;
  setOn: Function;
  setOff: Function;
}

const StatusContext = React.createContext<StatusContextProps>({
  isOn: false,
  flipIsOn: () => {},
  setOn: () => {},
  setOff: () => {},
});

export default StatusContext;