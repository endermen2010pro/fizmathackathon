import './index.css'
import {Routes, Route, Link, Navigate} from 'react-router-dom'
import { HomePage } from './pages/HomePage';
import { MapPage } from './pages/MapPage';
import { NotFoundPage } from './pages/NotFoundPage';

function App() {
  return (
    <>
      {/* <Route path="/" element={<Layout />}> */} {/* </Route> */}
      <Routes>
        
        <Route path="/" element={<HomePage />}/>
        <Route path='*' element={<NotFoundPage />}/>
        
      </Routes>
    </>
  );
}
export default App