import type {ButtonHTMLAttributes, ReactNode} from 'react'
import styles from './RoundButton.module.css'

// TODO design-check: no matching `round-button` component in Figma — add it there or remove this code.
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
