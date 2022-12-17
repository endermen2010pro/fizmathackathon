import rect from '../img/rect.png'
const MyCard = ({title}) => {
    return (
        <div className='card'>
            <img src={rect} alt="" className='cardImg' style={{"borderRadius":"9px"}}/>
            <h1 className='cardTitle'>Map</h1>
        </div>
    )
}

export {MyCard}