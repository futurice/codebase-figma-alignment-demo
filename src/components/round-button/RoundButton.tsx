import type {ButtonHTMLAttributes, ReactNode} from 'react'
import styles from './RoundButton.module.css'

type Props = ButtonHTMLAttributes<HTMLButtonElement> & {
  children: ReactNode
}

export function RoundButton({ className, children, ...rest }: Props) {
  const cls = [styles.roundButton, className].filter(Boolean).join(' ')
  return (
    <button type="button" className={cls} {...rest}>
      {children}
    </button>
  )
}
