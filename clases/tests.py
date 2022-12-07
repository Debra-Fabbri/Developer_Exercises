import unittest
import clases as cl

class developer_exercises_clases(unittest.TestCase):

    def  test_EjercicioClases_01(self):
        valor_test = cl.EjercicioClases(5,2)
        valor_esperado1 = [78.53981633974483 , 31.41592653589793]
        self.assertEqual(valor_test, valor_esperado1)
    
    def  test_EjercicioClases_02(self):
        valor_test = cl.EjercicioClases(5.8,2)
        valor_esperado = [105.68317686676065, 36.4424747816416]
        self.assertEqual(valor_test, valor_esperado)
    
    def  test_EjercicioClases_03(self):
        valor_test = cl.EjercicioClases(-5,2)
        valor_esperado = None
        self.assertEqual(valor_test, valor_esperado)



resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))
