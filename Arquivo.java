public class Arquivo {
	public static void main (String[] args ) {
	
	double peso;
	double altura;
	double imc;

	peso = 104;
	altura = 1.70;
	imc = peso / (altura * altura);

	if (imc < 16) {
		System.out.println("Baixo peso: grau 1");
	}
	else if (imc >= 16 && imc < 17) {
		System.out.println("Baixo peso: grau 2");
	}
	else if (imc >= 17 && imc < 18.50) {
		System.out.println("Baixo peso: grau 3");
	}
	else if (imc >= 18.50 && imc < 25) {
		System.out.println("Peso adequado"); 
	}
	else if (imc >= 25 && imc < 30) {
		System.out.println("Sobrepeso");
	}
	else if (imc >= 30 && imc < 35) {
		System.out.println("Obesidade: grau 1");
	}
	else if (imc >= 35 && imc < 40) {
		System.out.println("Obesidade: grau 2");
	}
	else if (imc >= 40) {
		System.out.println("Obesidade: grau 3");
	}


		System.out.println("Seu peso é: "+peso);
		System.out.println("Sua altura é: "+altura);
		System.out.println("O valor de seu índice de massa corporal é: "+imc);
	}
}