import { Link } from 'react-router-dom'
import line from '../img/line.png'
import sun from '../img/sun.png'
import rect from '../img/rect.png'
import { Miniinfo } from '../components/Miniinfo'
import { Card } from 'react-bootstrap'
import { MyCard } from '../components/MyCard'

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
                    {/* <div className='miniInfo'>
                        <img src={sun} alt="" className='sun'/>
                        <div>
                            <h1>First</h1>
                            <p>3400 +</p>
                        </div>
                    </div>
                    <div className='miniInfo'>
                        <img src={sun} alt="" className='sun'/>
                        <div>
                            <h1>Second</h1>
                            <p>Hello World!</p>
                        </div>
                    </div>
                    <div className='miniInfo'>
                        <img src={sun} alt="" className='sun'/>
                        <div>
                            <h1>Hello</h1>
                            <p>projects</p>
                        </div>
                    </div> */}
                    <Miniinfo title="First" body="Projects" color="#FF6853" />
                    <Miniinfo title="First" body="Projects" color="#80D2C4" />
                    <Miniinfo title="First" body="Projects" color="#80D2C4" />
                    <Miniinfo title="First" body="Projects" color="#80D2C4" />
                </div>
                <div className='cards'>
                    <h1 style={{"textAlign":"center", "color":"#D9D9D9", "marginBottom":"150px"}}>Opportunities</h1>
                    <div className='navBlock'>
                        {/* <div className='card'>
                            <img src={rect} alt="" className='cardImg'/>
                            <h1 className='cardTitle'>Map</h1>
                        </div>
                        <div className='card'>
                            <img src={rect} alt="" className='cardImg'/>
                            <h1 className='cardTitle'>Map</h1>
                        </div>
                        <div className='card'>
                            <img src={rect} alt="" className='cardImg'/>
                            <h1 className='cardTitle'>Map</h1>
                        </div>
                        <div className='card'>
                            <img src={rect} alt="" className='cardImg'/>
                            <h1 className='cardTitle'>Map</h1>
                        </div> */}
                        <MyCard title="Map"/>
                        <MyCard title="Map"/>
                        <MyCard title="Map"/>
                        <MyCard title="Map"/>
                    </div>
                </div>
                <h1>sadasd</h1>
                
            </div>
        </div>
        
    )
}

export {HomePage}