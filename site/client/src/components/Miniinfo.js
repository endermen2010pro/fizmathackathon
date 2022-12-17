import sun from '../img/sun.png'
const Miniinfo = ({title, body, color}) => {
    return (
        <div className='miniInfo'>
            <div style={{"backgroundColor":`${color}`, "width":'65px', "height":"65px","display":"flex", "justifyContent":"center", "alignItems":"center", "borderRadius":"9px"}}>
                <img src={sun} alt="" className='sun' style={{"width":'45px', "height":"45px"}}/>
            </div>
            
            <div>
                <h1>{title}</h1>
                <p>{body}</p>
            </div>
        </div>
    )
}

export {Miniinfo}