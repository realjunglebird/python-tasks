### Задача №6

Реализовать целочисленную функцию, вычисляющую _ψ_ на основе входного множества:

$$
\psi = |\Xi \cup \Nu| + \prod_{\nu \in \Nu} 4\nu, где \\
\Beta = \{ \eta + \eta^4 : \eta \in \Eta \land (\eta>1 \lor \eta\leq-56 ) \}, \\
\Nu = \{ \lceil \mu/2 \rceil : \mu\in\Mu \land \mu \leq 43\land\mu\geq-95 \}, \\
\Theta = \{\eta\mod3 : \eta \in \Eta \land \eta > -5 \land \eta < 45\}, \\
\Mu = \eta \cup \Beta, \\
\Xi = \{ \beta\mu : \beta\in\Beta \land \mu\in\Mu \land \beta \geq \mu \}.
$$

Примеры результатов вычислений:  
`main({-89, -25, 7, -51, -48, -12, -42, -72, -70, 62}) = 25`  
`main({4, -27, 7, -56, 40, 75, -76, 86, 27, -99}) = 56`