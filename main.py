if __name__ == '__main__':
        # Mostrar datos en tabla 
        import yfinance as yf

        # Datos del día "BBVA"
        print("---------Tabla de precios Banco BBVA----------\n")
        BBVA_precios = yf.download("BBVA", period='1d')
        print (BBVA_precios)
        print("\n")

        # Datos del día "Banco Santander"
        print("---------Tabla de precios Banco Santander----------\n")
        SAN_precios= yf.download("SAN", period= '1d')
        print(SAN_precios)
        print("\n")

        # Datos del día "Telefónica"
        print("---------Tabla de precios Telefónica----------\n")
        TEF_precios= yf.download("TEF", period= '1d')
        print(TEF_precios)
        print("\n")

        # Datos del día "Arcelormittal"
        print("---------Tabla de precios Arcelomittal----------\n")
        MT_precios= yf.download("MT", period= '1d')
        print(MT_precios)
        print("\n")

      





