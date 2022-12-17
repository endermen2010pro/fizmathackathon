import { Link } from 'react-router-dom'
import line from '../img/line.png'

const HomePage = () => {
    return (
        <div>
            <div className='firstBlock'>
                <div className='header'>
                    <h1> lgnis </h1>
                    <img src={line} alt="" className='headerLine'/>
                    <p className='paragraphHeader'>Description and other things. I don’t know what should be there. Just some text without any meaning.</p>
                </div>
            </div>
            <div className='SecondBlock'>
                <div className='info'>
                    <h1>First</h1>
                    <h1>Second</h1>
                    <h1>Third</h1>
                </div>
                <h1 style={{"textAlign":"center", "color":"#D9D9D9"}}>Opportunities</h1>
                <div className='navBlock'>
                    
                    <h1>Map</h1>
                    <h1>Map</h1>
                    <h1>Map</h1>
                </div>
            </div>
        </div>
        
    )
}

export {HomePage}