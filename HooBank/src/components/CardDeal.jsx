import { card } from '../assets';
import styles, { layout } from '../style';
import Button from "./Button";

const CardDeal = () => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
    <h2 className={`${styles.heading2}`}>
        Find a better card deal <br className="sm:block hidden" /> in few easy steps.
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illo fuga, reiciendis vitae ipsam iusto voluptatibus accusantium odit pariatur ab porro?
      </p>

      <Button styles={`mt-10`} />
    </div>

    <div className={layout.sectionImg}>
      <img src={card} alt="card" className="w-[90%] h-[90%] object-contain" />
    </div>
  </section>
)


export default CardDeal
